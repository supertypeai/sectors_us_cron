Use Github action to perform specific SQL function. `pg_cron` is not available on Neon, so we need this repo as an extrenal scheduler.  
Example usage for `cron_function.py`: 
```
python cron_function.py --name update_price_chg_30d
python cron_function.py --name function_name --args arg1 arg2 arg3
```
