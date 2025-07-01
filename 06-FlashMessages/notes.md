# Day 6 - Flash Messages  
  
## What are Flash Messages?  
- Used to show temporary messages (e.g. login success/failure).  
- Message persists for only one request.  
- Requires `secret_key` because messages are stored in session.  
  
## How to Use  
1. Set `app.secret_key`  
2. Use `flash(message, category)` to store a message  
3. Use `get_flashed_messages(with_categories=True)` in template to show it  
  
## Categories (for styling)  
- `success` → green  
- `danger` → red  
- `info` → blue  
- `warning` → yellow  
  
## Example:  
```python  
flash("Login successful!", "success")  
flash("Invalid username or password", "danger")  
