CREATE TABLE LXCItems (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  cpu_usage INT,
  memory_usage INT,
  created_timestamp BIGINT,
  status VARCHAR(50)
);

CREATE TABLE Networks (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  ip_address VARCHAR(45)
);

CREATE TABLE LXCItems_Networks (
  lxc_item_id INT UNSIGNED,
  network_id INT UNSIGNED,
  PRIMARY KEY (lxc_item_id, network_id),
  FOREIGN KEY (lxc_item_id) REFERENCES LXCItems(id),
  FOREIGN KEY (network_id) REFERENCES Networks(id)
);
