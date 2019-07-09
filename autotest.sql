/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 80015
Source Host           : localhost:3306
Source Database       : autotest

Target Server Type    : MYSQL
Target Server Version : 80015
File Encoding         : 65001

Date: 2019-07-09 16:33:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for apitest_apis
-- ----------------------------
DROP TABLE IF EXISTS `apitest_apis`;
CREATE TABLE `apitest_apis` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apiname` varchar(100) NOT NULL,
  `apiurl` varchar(200) NOT NULL,
  `apiparamvalue` varchar(800) NOT NULL,
  `apimethod` varchar(200) DEFAULT NULL,
  `apitester` varchar(16) DEFAULT NULL,
  `apiresult` varchar(200) NOT NULL,
  `apiresponse` varchar(5000) DEFAULT NULL,
  `apistatus` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `Product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `apitest_apis_Product_id_d86ce861_fk_product_product_id` (`Product_id`),
  CONSTRAINT `apitest_apis_Product_id_d86ce861_fk_product_product_id` FOREIGN KEY (`Product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_apis
-- ----------------------------
INSERT INTO `apitest_apis` VALUES ('1', '登录', '127.0.0.1:8000/login', 'null', 'get', 'tangky', 'login', 'null', '1', '2019-07-09 05:49:57.345000', '4');

-- ----------------------------
-- Table structure for apitest_apistep
-- ----------------------------
DROP TABLE IF EXISTS `apitest_apistep`;
CREATE TABLE `apitest_apistep` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apiname` varchar(100) NOT NULL,
  `apiurl` varchar(200) NOT NULL,
  `apistep` varchar(100) DEFAULT NULL,
  `apiparamvalue` varchar(800) NOT NULL,
  `apimethod` varchar(200) DEFAULT NULL,
  `apiresult` varchar(200) NOT NULL,
  `apiresponse` varchar(5000) DEFAULT NULL,
  `apiteststatus` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `Apitest_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `apitest_apistep_Apitest_id_ceefdb33_fk_apitest_apitest_id` (`Apitest_id`),
  CONSTRAINT `apitest_apistep_Apitest_id_ceefdb33_fk_apitest_apitest_id` FOREIGN KEY (`Apitest_id`) REFERENCES `apitest_apitest` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_apistep
-- ----------------------------
INSERT INTO `apitest_apistep` VALUES ('1', '登录', '127.0.0.1:8000/login', 'null', '33', 'get', '1', '1', '0', '2019-07-09 03:16:23.935000', '1');

-- ----------------------------
-- Table structure for apitest_apitest
-- ----------------------------
DROP TABLE IF EXISTS `apitest_apitest`;
CREATE TABLE `apitest_apitest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `apitestname` varchar(64) NOT NULL,
  `apitestdesc` varchar(64) DEFAULT NULL,
  `apitester` varchar(16) NOT NULL,
  `apitestresult` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `Product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `apitest_apitest_Product_id_260d36dd_fk_product_product_id` (`Product_id`),
  CONSTRAINT `apitest_apitest_Product_id_260d36dd_fk_product_product_id` FOREIGN KEY (`Product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of apitest_apitest
-- ----------------------------
INSERT INTO `apitest_apitest` VALUES ('1', '登录购物支付', '测试流程接口', 'tangky', '0', '2019-07-09 03:16:23.934000', '4');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('14', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('16', 'Can view user', '4', 'view_user');
INSERT INTO `auth_permission` VALUES ('17', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('18', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('20', 'Can view content type', '5', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('21', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('22', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('24', 'Can view session', '6', 'view_session');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 产品管理', '7', 'add_product');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 产品管理', '7', 'change_product');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 产品管理', '7', 'delete_product');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 产品管理', '7', 'view_product');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 单一场景接口', '8', 'add_apis');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 单一场景接口', '8', 'change_apis');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 单一场景接口', '8', 'delete_apis');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 单一场景接口', '8', 'view_apis');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 流程场景接口', '9', 'add_apitest');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 流程场景接口', '9', 'change_apitest');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 流程场景接口', '9', 'delete_apitest');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 流程场景接口', '9', 'view_apitest');
INSERT INTO `auth_permission` VALUES ('37', 'Can add apistep', '10', 'add_apistep');
INSERT INTO `auth_permission` VALUES ('38', 'Can change apistep', '10', 'change_apistep');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete apistep', '10', 'delete_apistep');
INSERT INTO `auth_permission` VALUES ('40', 'Can view apistep', '10', 'view_apistep');
INSERT INTO `auth_permission` VALUES ('41', 'Can add bug管理', '11', 'add_bug');
INSERT INTO `auth_permission` VALUES ('42', 'Can change bug管理', '11', 'change_bug');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete bug管理', '11', 'delete_bug');
INSERT INTO `auth_permission` VALUES ('44', 'Can view bug管理', '11', 'view_bug');
INSERT INTO `auth_permission` VALUES ('45', 'Can add 系统设置', '12', 'add_set');
INSERT INTO `auth_permission` VALUES ('46', 'Can change 系统设置', '12', 'change_set');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete 系统设置', '12', 'delete_set');
INSERT INTO `auth_permission` VALUES ('48', 'Can view 系统设置', '12', 'view_set');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$150000$jTcJ5Qiy5EvG$dEozSUN1f+ECWG2O22bwW/mHRz8FXapTgqqGrE5Yf04=', '2019-07-09 05:28:44.745000', '1', 'admin', '', '', '', '1', '1', '2019-07-09 01:33:21.287000');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for bug_bug
-- ----------------------------
DROP TABLE IF EXISTS `bug_bug`;
CREATE TABLE `bug_bug` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bugname` varchar(64) NOT NULL,
  `bugdetail` varchar(200) NOT NULL,
  `bugstatus` varchar(200) DEFAULT NULL,
  `buglevel` varchar(200) DEFAULT NULL,
  `bugcreater` varchar(200) NOT NULL,
  `bugassign` varchar(200) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `Product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `bug_bug_Product_id_5f035205_fk_product_product_id` (`Product_id`),
  CONSTRAINT `bug_bug_Product_id_5f035205_fk_product_product_id` FOREIGN KEY (`Product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bug_bug
-- ----------------------------
INSERT INTO `bug_bug` VALUES ('1', 'a', 'test', '激活', '3', 'fin', 'fin', '2019-07-09 06:41:54.753000', '4');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-07-09 01:37:21.697000', '1', 'web产品', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-07-09 01:37:44.759000', '2', '自动化平台', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-07-09 01:38:05.365000', '3', 'app产品', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-07-09 01:38:17.795000', '4', '商城', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-07-09 03:16:23.936000', '1', '登录购物支付', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"apistep\", \"object\": \"null\"}}]', '9', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-07-09 05:49:57.346000', '1', '登录', '1', '[{\"added\": {}}]', '8', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-07-09 06:41:54.753000', '1', 'a', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-07-09 06:50:49.391000', '1', 'seturl', '1', '[{\"added\": {}}]', '12', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('8', 'apitest', 'apis');
INSERT INTO `django_content_type` VALUES ('10', 'apitest', 'apistep');
INSERT INTO `django_content_type` VALUES ('9', 'apitest', 'apitest');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('11', 'bug', 'bug');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('7', 'product', 'product');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('12', 'set', 'set');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-07-09 01:30:19.882000');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-07-09 01:30:22.524000');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-07-09 01:30:33.927000');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-07-09 01:30:36.886000');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0003_logentry_add_action_flag_choices', '2019-07-09 01:30:37.044000');
INSERT INTO `django_migrations` VALUES ('6', 'contenttypes', '0002_remove_content_type_name', '2019-07-09 01:30:39.256000');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0002_alter_permission_name_max_length', '2019-07-09 01:30:40.498000');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0003_alter_user_email_max_length', '2019-07-09 01:30:41.898000');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0004_alter_user_username_opts', '2019-07-09 01:30:42.035000');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0005_alter_user_last_login_null', '2019-07-09 01:30:43.181000');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0006_require_contenttypes_0002', '2019-07-09 01:30:43.262000');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0007_alter_validators_add_error_messages', '2019-07-09 01:30:43.409000');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0008_alter_user_username_max_length', '2019-07-09 01:30:44.864000');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0009_alter_user_last_name_max_length', '2019-07-09 01:30:46.299000');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0010_alter_group_name_max_length', '2019-07-09 01:30:47.572000');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0011_update_proxy_permissions', '2019-07-09 01:30:47.635000');
INSERT INTO `django_migrations` VALUES ('17', 'product', '0001_initial', '2019-07-09 01:30:48.183000');
INSERT INTO `django_migrations` VALUES ('18', 'product', '0002_auto_20190708_2040', '2019-07-09 01:30:49.544000');
INSERT INTO `django_migrations` VALUES ('19', 'product', '0003_auto_20190708_2041', '2019-07-09 01:30:49.615000');
INSERT INTO `django_migrations` VALUES ('20', 'product', '0004_auto_20190708_2044', '2019-07-09 01:30:50.988000');
INSERT INTO `django_migrations` VALUES ('21', 'sessions', '0001_initial', '2019-07-09 01:30:51.814000');
INSERT INTO `django_migrations` VALUES ('22', 'apitest', '0001_initial', '2019-07-09 03:07:26.770000');
INSERT INTO `django_migrations` VALUES ('23', 'apitest', '0002_auto_20190709_1345', '2019-07-09 05:45:58.581000');
INSERT INTO `django_migrations` VALUES ('24', 'apitest', '0003_auto_20190709_1422', '2019-07-09 06:22:34.369000');
INSERT INTO `django_migrations` VALUES ('25', 'bug', '0001_initial', '2019-07-09 06:40:39.635000');
INSERT INTO `django_migrations` VALUES ('26', 'bug', '0002_auto_20190709_1442', '2019-07-09 06:42:55.388000');
INSERT INTO `django_migrations` VALUES ('27', 'set', '0001_initial', '2019-07-09 06:50:12.910000');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('c7m2zl1ci89cu6zekjsyjvv2575m7gf7', 'OTI0ZDUyOGZjZTVlM2Q3MTk0YjVjODZhZGE2Njk0YTFlNjk5NDFiNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2M2EwM2I5MTIyZTFiNmYyMjlkOTc3OWQ3NWQyYTY4MTdiOGUxZjMwIiwidXNlciI6ImFkbWluIn0=', '2019-07-23 05:28:44.822000');

-- ----------------------------
-- Table structure for product_product
-- ----------------------------
DROP TABLE IF EXISTS `product_product`;
CREATE TABLE `product_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `productname` varchar(64) NOT NULL,
  `producter` varchar(200) NOT NULL,
  `productdesc` varchar(200) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_product
-- ----------------------------
INSERT INTO `product_product` VALUES ('1', 'web产品', 'tangky', '百度搜索', '2019-07-09 01:37:21.696000');
INSERT INTO `product_product` VALUES ('2', '自动化平台', 'tangky', '包括API,WebUI,AppUI自动化测试', '2019-07-09 01:37:44.758000');
INSERT INTO `product_product` VALUES ('3', 'app产品', 'tangky', '计算器,Csdn', '2019-07-09 01:38:05.364000');
INSERT INTO `product_product` VALUES ('4', '商城', 'tangky', '图书', '2019-07-09 01:38:17.794000');

-- ----------------------------
-- Table structure for set_set
-- ----------------------------
DROP TABLE IF EXISTS `set_set`;
CREATE TABLE `set_set` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `setname` varchar(64) NOT NULL,
  `setvalue` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of set_set
-- ----------------------------
INSERT INTO `set_set` VALUES ('1', 'seturl', '127.0.0.1:8000');
