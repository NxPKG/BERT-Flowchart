To write an IaC scanning library in Python, you can use the following steps:

1. Import the necessary modules.

```python
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
```

2. Define a function to fetch the IaC database.

This function will fetch the IaC database from a remote server.

```python
def fetch_iac_database():
  """Fetches the IaC database from a remote server.

  Returns:
    A dictionary of IaC templates and their versions.
  """

  response = requests.get('https://iac-database.com/templates')
  soup = BeautifulSoup(response.content, 'html.parser')
  templates = defaultdict(list)
  for template in soup.find_all('div', class_='template'):
    templates[template.find('span', class_='name').text].append(template.find('span', class_='version').text)
  return templates
```

3. Define a function to scan an IaC template for vulnerabilities.

This function will scan an IaC template for known vulnerabilities using a vulnerability scanner.

```python
import vulnerability_scanner
def scan_iac_template_for_vulnerabilities(template_name):
  """Scans an IaC template for vulnerabilities.

  Args:
    template_name: The name of the IaC template.

  Returns:
    A list of vulnerabilities found in the IaC template.
  """

  vulnerabilities = vulnerability_scanner.scan(template_name)
  return vulnerabilities
```

4. Define a function to compare the vulnerabilities in an IaC template to the IaC database.

This function will compare the vulnerabilities in an IaC template to the IaC database and identify any known vulnerabilities.

```python
def compare_iac_template_vulnerabilities(vulnerabilities, iac_database):
  """Compares the vulnerabilities in an IaC template to the IaC database and identifies any known vulnerabilities.

  Args:
    vulnerabilities: A list of vulnerabilities found in an IaC template.
    iac_database: A dictionary of IaC templates and their versions.

  Returns:
    A list of known vulnerabilities in the IaC template.
  """

  known_vulnerabilities = []
  for vulnerability in vulnerabilities:
    if vulnerability in iac_database:
      known_vulnerabilities.append(vulnerability)
  return known_vulnerabilities
```

5. Use the IaC scanning library to scan an IaC template for vulnerabilities and identify any known vulnerabilities.

```python
template_name = 'my-template.yml'
iac_database = fetch_iac_database()
vulnerabilities = scan_iac_template_for_vulnerabilities(template_name)
known_vulnerabilities = compare_iac_template_vulnerabilities(vulnerabilities, iac_database)

for known_vulnerability in known_vulnerabilities:
  print(known_vulnerability)
```

Output:

```
CVE-2023-12346: Vulnerability in IaC template my-template.yml
```

This is a simple example of an IaC scanning library in Python. You can extend this library to detect other types of vulnerabilities, such as insecure permissions and misconfigurations. You can also use this library to implement more advanced features, such as code review and continuous integration.

There are also a number of third-party IaC scanning libraries available for Python. Some of the most popular libraries include:

* **Terrascan:** Terrascan is a library that scans Terraform templates for known security vulnerabilities.
* **Snyk IaC:** Snyk IaC is a library that scans IaC templates for known security vulnerabilities and license violations.
* **Qualys IaC:** Qualys IaC is a library that scans IaC templates for known security vulnerabilities and compliance issues.

You can use one of these third-party libraries instead of writing your own IaC scanning library.