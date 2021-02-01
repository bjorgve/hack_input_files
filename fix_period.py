import json
def fix_period(template, period):
    with open(template, 'r') as input:
        mrchem = json.load(input)
        mrchem['Periodic']['period'] = [period]*3
    with open(template, 'w') as output:
        mrchem = json.dump(mrchem, output, indent=2)
