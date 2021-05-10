TRUNCATE TABLE products_producttag RESTART IDENTITY CASCADE;
TRUNCATE TABLE products_productmanufacturer RESTART IDENTITY CASCADE;

INSERT INTO user_address ("country", "city", "houseNumber", "streetName", "postNumber") VALUES
('Iceland', 'Hafnarfjörður', 22, 'Blikaás', 221),
('Iceland', 'Reykjavík', 16, 'Austurstræti', 101),
('Iceland', 'Hafnarfjörður', 16, 'Breiðvangur', 220),
('Iceland', 'Hafnarfjörður', 41, 'Miðvangur', 220);

INSERT INTO user_profile ("name", "email", "phone", "photo", "address_id", "user_id") VALUES
('Daníel Örn Sigurðsson', 'daniels19@ru.is', 6986320, 'https://miniblogcore.azurewebsites.net/blog/some-url/', 1, 1),
('Garpur Hnévill', 'garpurH19@ru.is', 6986321, 'https://miniblogcore.azurewebsites.net/blog/some-url/', 2, 2),
('Jón Jónsson', 'jón19@ru.is', 6986327, 'https://miniblogcore.azurewebsites.net/blog/some-url/', 3, 3),
('Gunnar Ingvarsson', 'gunnar19@ru.is', 6986323, 'https://miniblogcore.azurewebsites.net/blog/some-url/', 4, 4);

INSERT INTO products_productmanufacturer (name) VALUES
('General Mills'),
('Kellogg''s'),
('Orkla');

INSERT INTO products_producttag (name) VALUES
('Healthy'),
('Sugary');

INSERT INTO products_product (name, price, description, "nutriInfo", amount, manufacturer_id, tag_id) VALUES
('Cheerios', 700, 'Part of a balanced breakfast', 'Carbs and stuff', 23, 1, 1),
('Honey Nut Cheerios', 800, 'A weekend breakaway from the regular kind', 'Carbs and sugar', 16, 1, 2),
('Cocoa Puffs', 850, 'I''m going cuckoo for it', 'Carbs, sugar and cocoa', 4, 1, 2),
('Lucky Charms', 900, 'Keep them all to yourself', 'Carbs and sugar', 5, 1, 2),
('Havre Fras', 750, 'Ta en pute når du våkner ', 'Carbs and stuff', 17, 3, 1),
('Cinnamon Toast Crunch', 800, 'Reminds you of better times', 'Carbs, sugar and cinnamon', 10, 1, 2),
('Trix', 850, 'Adolescents and adults away', 'Carbs and sugar', 22, 1, 2),
('Froot Loops', 800, 'Pssst... they all taste the same regardless of the color', 'Carbs and sugar', 16, 1, 2),
('Rice Krispies', 650, 'You can really taste the crackle', 'Carbs and stuff', 28, 2, 1);

INSERT INTO products_productimage (image, product_id) VALUES
('https://images-na.ssl-images-amazon.com/images/I/81VQIHQ0-CL._SL1500_.jpg', 1),
('https://d3d71ba2asa5oz.cloudfront.net/12026801/images/honeynutcheeriosce_e780e_generalmills_alwaysfre_128__1.jpg', 2),
('https://i5.walmartimages.com/asr/e78f3d25-baed-4d09-bb70-ea2ea8e3f594.93489774c0a84ad9c0170cb59ef27bc0.jpeg', 3),
('https://i5.walmartimages.com/asr/66e3fc3d-32ef-41b4-9aa3-2852b3c17f19_1.f19a53b164c8a56d749fb11670983422.jpeg', 4),
('https://cdn.shopify.com/s/files/1/1518/6272/products/To-1.01_Flingorhavrefrasoriginal_1024x1024.jpg?v=1520345667', 5),
('https://www.usa-drinks.de/media/image/product/12475/lg/cinnamon-toast-crunch-1-x-340g.jpg', 6),
('https://i5.walmartimages.com/asr/20011f44-8b7e-4750-a37a-236fbba4e54c_1.9b22a7ddf3a4198b5e8f2a7cc7836557.jpeg', 7),
('https://www.frajosfood.com/img/p/3/7/0/0/8/37008-thickbox_default.jpg', 8),
('https://images-na.ssl-images-amazon.com/images/I/91EbJNh%2BkuL._SL1500_.jpg', 9);

--INSERT INTO cart_orderitem(quantity, order_id, product_id) VALUES
--(2, 1, 1),
--(1, 1, 9);


INSERT INTO user_order ("status", "profile_id") VALUES ('done', 1);
INSERT INTO user_order ("status", "profile_id") VALUES ('done', 1);
INSERT INTO user_order ("status", "profile_id") VALUES ('done', 1);
INSERT INTO user_order ("status", "profile_id") VALUES ('in progress', 1);

INSERT INTO user_paymentinfo ("cardHolder", "cardNumber", "expDate", "cvc", "profile_id") VALUES ('Daníel Örn Sigurðsson', 1234 5678 1111 1111, '1221', 121, 1);
INSERT INTO user_paymentinfo ("cardHolder", "cardNumber", "expDate", "cvc", "profile_id") VALUES ('Garpur Hnévill', 1234 5678 2222 2222, '0522', 122, 2);
INSERT INTO user_paymentinfo ("cardHolder", "cardNumber", "expDate", "cvc", "profile_id") VALUES ('Jón Jónsson', 1234 5678 3333 3333, '0523', 124, 3);
INSERT INTO user_paymentinfo ("cardHolder", "cardNumber", "expDate", "cvc", "profile_id") VALUES ('Gunnar Ingvarsson', 1234 5678 4444 4444, '0524', 124, 4);

INSERT INTO user_searchhistory ("query", "date", "profile_id") VALUES ('Daníel Örn Sigurðsson', 21, 1);
INSERT INTO user_searchhistory ("query", "date", "profile_id") VALUES ('Garpur Hnévill', 22, 2);
INSERT INTO user_searchhistory ("query", "date", "profile_id") VALUES ('Jón Jónsson', 23, 3);
INSERT INTO user_searchhistory ("query", "date", "profile_id") VALUES ('Gunnar Ingvarsson', 24, 4);

INSERT INTO cart_orderitem ("quantity", "user_order_id", "product_id") VALUES ('2', 1, 1);
INSERT INTO cart_orderitem ("quantity", "user_order_id", "product_id") VALUES ('2', 1, 2);
INSERT INTO cart_orderitem ("quantity", "user_order_id", "product_id") VALUES ('1', 2, 3);
INSERT INTO cart_orderitem ("quantity", "user_order_id", "product_id") VALUES ('1', 4, 4);
