from client import exceptions as ex
import collections

###############
# Field types #
###############

class NoValue(object):
    pass

NoValue = NoValue()

class Field(object):
    _default = NoValue

    def __init__(self, optional=False, **kargs):
        self._optional = optional
        if 'default' in kargs:
            value = kargs['default']
            if not self.is_valid(value):
                raise ex.SerializeException('Invalid default: {}'.format(value))
            self._optional = True
            self._default = value

    @property
    def optional(self):
        return self._optional

    @property
    def default(self):
        return self._default

    def is_valid(self, value):
        """Subclasses should override this method for field validation."""
        return True

    def coerce(self, value):
        """Subclasses should override this method for type coercion.

        Default version will simply return the argument. If the argument
        is not valid, a SerializeException is raised.

        For primitives like booleans, ints, floats, and strings, use
        this default version to avoid unintended type conversions."""
        if not self.is_valid(value):
            raise ex.SerializeException('{} is not a valid value for '
                                        'type {}'.format(value, self.__class__.__name__))
        return value

    def to_json(self, value):
        """Subclasses should override this method for JSON encoding."""
        if not self.is_valid(value):
            raise ex.SerializeException('Invalid value: {}'.format(value))
        return value

class Boolean(Field):
    def is_valid(self, value):
        return value in (True, False)

class Int(Field):
    def is_valid(self, value):
        return type(value) == int

class Float(Field):
    def is_valid(self, value):
        return type(value) in (int, float)

class String(Field):
    def is_valid(self, value):
        return type(value) == str

class List(Field):
    def __init__(self, type=None, **kargs):
        """Constructor for a List field.

        PARAMETERS:
        type -- type; if type is None, the List can be heterogeneous.
                Otherwise, the List must be homogeneous with elements
                of the specified type.
        """
        super().__init__(**kargs)
        self._type = type

    def is_valid(self, value):
        valid = type(value) == list
        if self._type is not None:
            valid &= all(isinstance(e, self._type) for e in value)
        return valid

    def coerce(self, value):
        if self._type is None:
            try:
                return list(value)
            except TypeError as e:
                raise ex.SerializeException(str(e))
        else:
            # TODO(albert): find a way to do better element-wise type coercion
            # so that constructors can take additional arguments
            try:
                return [self._type(elem) for elem in value]
            except TypeError as e:
                raise ex.SerializeException(str(e))

    def to_json(self, value):
        value = super().to_json(value)
        return [elem.to_json() if hasattr(elem, 'to_json') else elem
                             for elem in value]

class Dict(Field):
    def __init__(self, keys=None, values=None, ordered=False, **kargs):
        super().__init__(**kargs)
        self._keys = keys
        self._values = values
        self._constructor = collections.OrderedDict if ordered else dict
        self._ordered = ordered

    @property
    def ordered(self):
        return self._ordered

    def is_valid(self, value):
        valid = isinstance(value, dict)
        if self._keys is not None:
            valid &= all(isinstance(k, self._keys) for k in value)
        if self._values is not None:
            valid &= all(isinstance(v, self._values) for v in value.values())
        return valid

    def coerce(self, value):
        try:
            coerced = self._constructor(value)
        except TypeError as e:
            raise ex.SerializeException(str(e))

        result = self._constructor()
        for k, v in coerced.items():
            if self._keys is not None:
                k = self._keys(k)
            elif self._values is not None:
                v = self._values(k)
            result[k] = v
        return result

    def to_json(self, value):
        value = super().to_json(value)
        result = self._constructor()
        for k, v in value.items():
            if hasattr(k, 'to_json'):
                k = k.to_json()
            if hasattr(v, 'to_json'):
                v = v.to_json()
            result[k] = v
        return result

########################
# Serializable Objects #
########################

class _SerializeMeta(type):
    def __init__(cls, name, bases, attrs):
        type.__init__(cls, name, bases, attrs)
        cls._fields = {}
        for base in bases:
            if hasattr(base, '_fields'):
                cls._fields.update(base._fields)
        cls._fields.update({attr: value for attr, value in attrs.items()
                                        if isinstance(value, Field)})

    def __call__(cls, *args, **kargs):
        obj = type.__call__(cls, *args, **kargs)
        # Validate existing arguments
        for attr, value in kargs.items():
            if attr not in cls._fields:
                raise ex.SerializeException('__init__() got an unexpected '
                                'keyword argument: {}'.format(attr))
            else:
                setattr(obj, attr, value)
        # Check for missing/default fields
        for attr, value in cls._fields.items():
            if attr in kargs:
                continue
            elif value.optional:
                setattr(obj, attr, value.default)
            else:
                raise ex.SerializeException('__init__() missing expected '
                                'argument {}'.format(attr))
        obj.post_instantiation()
        return obj

class Serializable(metaclass=_SerializeMeta):
    def __init__(self, *args, **kargs):
        pass

    def __setattr__(self, attr, value):
        cls = type(self)
        if attr in cls._fields:
            field = cls._fields[attr]
            if value != NoValue and not field.is_valid(value):
                value = field.coerce(value)
        super().__setattr__(attr, value)

    def post_instantiation(self):
        """Subclasses can override this method to perform post-instantiation
        work.
        """
        pass

    def to_json(self):
        cls = type(self)
        json = {}
        for attr, field in cls._fields.items():
            value = getattr(self, attr)
            if not field.optional or value != NoValue:
                json[attr] = field.to_json(value)
        return json

