-- 演習2　pr0602-1.sql

CREATE DATABASE if not EXISTS pr0602;
use pr0602;
DROP TABLE if EXISTS salesdetail;
DROP TABLE if EXISTS customer;
DROP TABLE if EXISTS item;

CREATE TABLE item (
    itemID int not NULL auto_increment ,
    itemcode varchar(10) UNIQUE not NULL,
    iname varchar(100),
    unitprice int,
    maker varchar(50),
    lastupdate datetime,
    PRIMARY key(itemID)
);

CREATE TABLE customer(
    customerID int not NULL auto_increment,
    cname VARCHAR(50),
    caddress VARCHAR(100),
    tel VARCHAR(20),
    lastupdate datetime,
    PRIMARY key(customerID)
);

CREATE TABLE salesdetail(
    salesdetailID int not NULL auto_increment,
    itemcode VARCHAR(10) ,
    customerID int,
    quantity int,
    salesdate date,
    lastupdate datetime,
    PRIMARY key(salesdetailID),
    FOREIGN key(itemcode)
        REFERENCES item(itemcode)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN key(customerID)
        REFERENCES customer(customerID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

desc item;
desc customer;
desc salesdetail;
