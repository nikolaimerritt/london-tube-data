CREATE SCHEMA `tube_schema` ;
CREATE TABLE  `Station` (
	`station_id` varchar(32) not null,
	`station_name` varchar(256) not null,
	`latitude` decimal(3, 10) not null,
	`longitude` decimal(3, 10) not null,
	primary key (`station_id`)
);

CREATE TABLE `Line` (
	`line_name` varchar(256) not null,
	primary key (`line_name`)
);

CREATE TABLE `Connection` (
	`station_id` varchar(32) not null,
	`line_name` varchar(256) not null,
	
	constraint `station_id_constraint` foreign key (`station_id`) 
		references `Station` (`station_id`) on delete cascade,
	
	constraint `line_name_constraint` foreign key (`line_name`)
		references `Line` (`line_name`) on delete cascade,
	primary key (`station_id`, `line_name`)
)