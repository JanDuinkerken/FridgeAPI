CREATE TABLE Fridge(
    fridgeId bigint not null auto_increment,
    location varchar(50) not null,
    n_items smallint not null,
    constraint FridgePk primary key(fridgeId),
    constraint validNItems CHECK (n_items >= 0)
) engine=InnoDB

CREATE TABLE Item(
    itemId bigint not null auto_increment,
    fridgeId bigint not null,
    i_name varchar(50) not null,
    cuantity smallint not null,
    r_date datetime not null,
    constraint ItemPk primary key(itemId),
    constraint validCuantity CHECK (cuantity >= 0)
) engine=InnoDB

