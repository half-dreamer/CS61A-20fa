Place:
Instance Attributions:name, exit, bees, ant, entrance
method:add_insect(self, insect), remove_insect(self, insect), 

Insect:
Class Attributions: damage, is_watersafe
Instance Attributions: armor, place
method: reduce_armor(self, amount), action(self, gamestate), death_callback(self), add_to(self, place), remove_from(self, place)

Ant(Insect)
class attributions: implemented, food_cost, is_watersafe
method:can_contain(self, other), contain_ant(self, other), remove_ant(self, other), add_to(self, place), remove_from(self, place)

HarvesterAnt(Ant):
class attributions:name, implemented, food_cost
method:action(self, gamestate)

ThrowerAnt(Ant):
class attributions: name, implemented, damage, food_cost, distance, min_range, max_range
method:nearest_bee(self, beehive), throw_at(self, target), action(self, gamestate)

ShortThrower(ThrowerAnt):
class Attributions: name, food_cost, implemented, min_range, max_range

QueenAnt(ScubaThrower):
class Attributions:name, food_cost,implemented

LongThrower(ThrowerAnt):
class Attributions:name, food_cost, implemented, in_range, max_range

ScubaThrower(ThrowerAnt):
class Attritubtions: name, food_cost, implemented, is_watersafe

FireAnt(Ant):
class Attributions: name, damage, food_cost, implemented
method:__init__(self, armor=3), reduce_armor(self, amount)

HungryAnt(Ant):
class Attributions: name, food_cost, implemented, time_to_digest
Instance attributions: digesting
method:eat_bee(self, bee), action(self, gamestate)

WallAnt(Ant):
class Attritutions: name, food_cost, implemented
method:__init(self, armor=4)

-----------------------------

NinjaAnt(Ant):
name, damage, food_cost, implemented
method: action(self, gamestate)

ContainerAnt(Ant):
__init(self, *args, **kwargs)
method:can_contain(self, other), contain_ant(self, ant), remove_ant(self, ant), remove_from(self, place), action(self, gamestate)

BodyguardAnt(ContatinerAnt):
name, food_cost, implemented

TankAnt(ContatinerAnt):
name, damage, food_cost, implemented
method: __init__, action

SlowThrower(ThrowerAnt)
ScaryThrower(ThrowerAnt)
LaserAnt(ThrowerAnt)

---------------------


rANTdom_else_none(s)
AntRemover(Ant):remove the ant

---------------------

Bee(Insect):
class Attributions:name, damage, is_watersafe
method:sting(self, ant), move_to(self, place), blocked(self), action(self, gamestate), add_to(self, place), remove_from(self, place)

Wasp(Bee)
Hornet(Bee)
NinjaBee(Bee)
Boss(Wasp, Hornet)

--------------------

Hive(Place):
Instance Attributions:name, assault_plan, bees, entrance, ant, None
method:strategy(self, gamestate)

Water(Place):
method:add_insect(self, insect)

-------------

GameState:
Instance Attributions:time, food, strategy, beehive, ant_types, dimensions, active_bees, configure(beehive, create_places)
method: configure(self, beehive, create_places), simulate(self), deploy_ant(self, place_name, ant_type_name), remove_ant(self, palce_name)

AntHomeBase(Place):
method:add_insect(self, insect), ants_win(), bees_win(), ant_types()

GameOverException(Exception)
AntWinException(GameOverException)
BeeWinException(GameOverException)

interactive_strategy(gamestate)

----------

wet_layout
dry_layout
-----------

AssaultPlan:
method:add_wave


make_slow(action, bee)
make_scare(action, bee)
apply_status(status, bee, length)



class Bee(Insect):
    """A Bee moves from place to place, following exits and stinging ants."""

    name = 'Bee'
    damage = 1
    is_watersafe = True
    # OVERRIDE CLASS ATTRIBUTES HERE


    def sting(self, ant):
        """Attack an ANT, reducing its armor by 1."""
        ant.reduce_armor(self.damage)

    def move_to(self, place):
        """Move from the Bee's current Place to a new PLACE."""
        self.place.remove_insect(self)
        place.add_insect(self)

    def blocked(self):
        """Return True if this Bee cannot advance to the next Place."""
        # Special handling for NinjaAnt
        # BEGIN Problem Optional
        return self.place.ant is not None and self.place.ant.blocks_path 
        # END Problem Optional

    def action(self, gamestate):
        """A Bee's action stings the Ant that blocks its exit if it is blocked,
        or moves to the exit of its current place otherwise.

        gamestate -- The GameState, used to access game state information.
        """
        destination = self.place.exit
        # Extra credit: Special handling for bee direction
        # BEGIN EC
        "*** YOUR CODE HERE ***"
        # END EC
        if self.blocked():
            self.sting(self.place.ant)
        elif self.armor > 0 and destination is not None:
            self.move_to(destination)

    def add_to(self, place):
        place.bees.append(self)
        Insect.add_to(self, place)

    def remove_from(self, place):
        place.bees.remove(self)
        Insect.remove_from(self, place)
