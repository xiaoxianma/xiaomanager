# xiaomanager
A family life manager.

https://xiaomanager.herokuapp.com/

## Expense manager
This is one feature of xiaomanager. Manage family expense.

### Motivation
People usually have varieties of credit cards. They are offering benefits especially points or cash back in different categories such as restaurant, groceries, gas, travel, etc. Most people don't fully utilize the credit cards benefits from their credit cards pool due to improper credit cards use. This app is aiming to help people realize how much significantly they lost because of that.

### Main Features
- Expense visualization (Complete)
- Show current credit card benefits (Complete)
- Manage daily transactions including New/Modify/Delete (Complete)
- AI & Algorithm suggest the best payment(credit cards, debit card, cash, etc.) you need to make (TODO)
  * Support manual input merchant information
  * Support take a photo of merchant  
  Hight level strategy:
  1. Analyze category of the merchant
  2. Run this category and merchant throughout the credit card pool by category reward, special merchant offer, etc
  3. Drop selections if running out of max benefits limit such discover max $1500 purchase category, AXP BCP max $6000 supermarkets
  4. Pick the winner!
- Show how much money lose away from the best strategy (TODO)

## Asset portfolio manager
TODO

## Travel manager
TODO

## [Development Guide](https://github.com/xiaoxianma/xiaomanager/blob/fastapi/DEVELOPMENT_GUIDE.md)
