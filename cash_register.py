# The parameters are integers
def change(due , paid):
    if paid == due:
        return {}
    # Convert the cents
    change = (paid - due)

    # Return a dict of how many bills and coins to give back
    deno_rand = {20000: 0, 10000: 0, 5000: 0, 2000: 0, 1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0}
    deno = {}

    # Calculating the change and adding to empty dict
   
    if paid > due:
        for amount in deno_rand:
            while change >= amount:
                # Subracting from the change amount
                change -= amount
                # Adding to the key's value
                deno_rand[amount] += 1
        for amount in deno_rand:
            if deno_rand[amount] > 0:
                new_amount = amount
                deno.update({new_amount: deno_rand[amount]})      

        return deno

    else:
        print("Amount paid is too small.")


