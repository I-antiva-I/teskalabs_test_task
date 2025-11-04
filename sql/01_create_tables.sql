CREATE TABLE LXCItems (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(128),
  cpu_usage INT,
  memory_usage INT,
  created_timestamp BIGINT,
  status VARCHAR(32)
);


CREATE TABLE Networks (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(128),
  ip_address VARCHAR(64),
  lxc_item_id INT UNSIGNED,
  FOREIGN KEY (lxc_item_id) REFERENCES LXCItems(id)
);
