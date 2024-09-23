-- 코드를 입력하세요
SELECT USER_ID, PRODUCT_ID
FROM online_sale
GROUP BY user_id, product_id
HAVING count(*) >= 2
ORDER BY user_id, product_id DESC;