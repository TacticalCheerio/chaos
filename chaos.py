import requests

# TODO
# Add CLI flags
# Write API key to seperate file
# Wrap HTTP requests in a seperate function and build in retries and paging

headers = {
    'Authorization': 'API_KEY'
}


def fetch_count(domain=None):
    url = f'https://dns.projectdiscovery.io/dns/{domain}'

    r = requests.get(url, headers=headers)

    if r.ok:
        return r.json()
    else:
        return f'Error\nStatus Code: {r.status_code}\nResponse Body: {r.text}'


def fetch_hosts(domain=None):
    url = f'https://dns.projectdiscovery.io/dns/{domain}/subdomains'

    r = requests.get(url, headers=headers)

    if r.ok:
        return r.json()
    else:
        return f'Error\nStatus Code: {r.status_code}\nResponse Body: {r.text}'


def add_hosts():
    url = f'https://dns.projectdiscovery.io/dns/add'

    data = 'subs.txt'

    r = requests.post(url, headers=headers, data=data)

    if r.ok:
        return 'Data successfully added'
    else:
        return f'Error\nStatus Code: {r.status_code}\nResponse Body: {r.text}'


def recon_data():
    url = f'https://dns.projectdiscovery.io/dns/{domain}/public-recon-data'

    r = requests.get(url, headers=headers, data=data)

    if r.ok:
        return r.json()
    else:
        return f'Error\nStatus Code: {r.status_code}\nResponse Body: {r.text}'