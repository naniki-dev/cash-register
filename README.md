# Cash Register
 
Python function that calculates the change to return to a customer, broken down by bill/coin denomination.
 
## How it works
 
`change(due, paid)` takes two integers representing amounts in **cents**:
 
- `due` — the amount owed
- `paid` — the amount the customer handed over
It returns a dictionary mapping each denomination (in cents) to how many of that denomination should be given back.