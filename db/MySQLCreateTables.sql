CREATE DATABASE inventory;
USE inventory;

CREATE TABLE Fridge(
    fridgeId bigint not null auto_increment,
    location varchar(50) not null,
    constraint FridgePk primary key(fridgeId)
) engine=InnoDB;

CREATE TABLE Item(
    itemId bigint not null auto_increment,
    fridgeId bigint not null,
    i_name varchar(50) not null,
    cuantity smallint not null,
    r_date datetime not null,
    drawer smallint,
    constraint ItemPk primary key(itemId),
    constraint FridgeFK foreign key(fridgeId)
      references Fridge(fridgeId) on delete cascade,
    constraint validCuantity CHECK (cuantity >= 0),
    constraint validDrawer CHECK (drawer >= 0)
) engine=InnoDB;

