USE jobs;

CREATE TABLE `company` (
    `guid` char(32) PRIMARY KEY,
    `ad_img` varchar(500) DEFAULT NULL,
    `logo` varchar(500) DEFAULT NULL,
    `name` varchar(200) DEFAULT NULL,
    `tag_line` varchar(500) DEFAULT NULL,
    `status` varchar(40) DEFAULT NULL,
    `statements` varchar(4500) DEFAULT NULL,
    `tech_stack` varchar(2500) DEFAULT NULL,
    `tech_stack_tags` varchar(200) DEFAULT NULL,
    `benefits` varchar(400) DEFAULT NULL,
    `addresses` varchar(200) DEFAULT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
