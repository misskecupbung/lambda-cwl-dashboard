import json


public_key = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxDeya69pIjpCDWKNe959
i6znrDAfxFRzwxwcbOIopb3n9O0MH+aF3pKDZfphJm5xAET75DyBF8kC4cIvBZIk
tKI25FhOGso0oVkNzhFjK40sWE82vmm9dqBIkwDy3kH34NAnz0QjNDNGBVZxEA0b
7SzsWoL/C902zb9UZUlgFqAkAKKcFQHtrA3/Is6QDRkiPe4cY54ee2UpxSbGwvIj
zKbqesNGvuARcez2Yfvx3JqabeL1XK7fTXhVmHp0Fk8GB1+Y+6kjnZ4wVURqbFyn
xHiZyijtiHGFaHlXlfDowDZrnXce1rklCORET6PVhyQ7BnDwnt6NVogFEYVhWjvl
FwIDAQAB
-----END PUBLIC KEY-----
"""

def lambda_handler(event, context):
    # logs out to CloudWatch logs
    print(public_key)

    return {
        'statusCode': 200,
        'body': json.dumps(public_key)
    }