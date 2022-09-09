.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price
      from products
          group by category;

CREATE TABLE lowest_prices AS
  SELECT store,item,min(price)
  from inventory 
  group by item;

CREATE TABLE best_deals AS
  SELECT name as best_deal ,min(MSRP / rating) as deal_anticipation
  from products group by category;


CREATE TABLE shopping_list AS
  SELECT best_deal,store
  from lowest_prices,best_deals
  where item = best_deal;


CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs) 
  from shopping_list as a,stores as b
  where a.store = b.store;

