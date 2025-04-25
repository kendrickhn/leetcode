select round(
            100 * sum(
            case 
            when d.order_date = d.customer_pref_delivery_date then 1
            else 0
            end) / 
            count(distinct d.customer_id)
            ,2) as immediate_percentage
from Delivery d
left join (select customer_id, min(order_date) as fo
            from Delivery 
            group by 1) f
on d.customer_id = f.customer_id
where d.order_date = f.fo;