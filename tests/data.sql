INSERT INTO user (id, username, password)
VALUES
  (0, 'user1', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  (1, 'user2', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO alarm (id, created, enabled, days, hour, minute)
VALUES
  (0, '2021-03-05 10:40:37', true, 'Monday', 10, 30),
  (1, '2021-04-08 20:04:05', false, 'Tuesday', 8, 30);
