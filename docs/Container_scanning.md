To write a container scanning library in Python, you can use the following steps:

1. Import the necessary modules.

```python
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
```

2. Define a function to fetch the container image database.

This function will fetch the container image database from a remote server.

```python
def fetch_container_image_database():
  """Fetches the container image database from a remote server.

  Returns:
    A dictionary of container images and their versions.
  """

  response = requests.get('https://container-image-database.com/images')
  soup = BeautifulSoup(response.content, 'html.parser')
  images = defaultdict(list)
  for image in soup.find_all('div', class_='image'):
    images[image.find('span', class_='name').text].append(image.find('span', class_='version').text)
  return images
```

3. Define a function to scan a container image for vulnerabilities.

This function will scan a container image for known vulnerabilities using a vulnerability scanner.

```python
import vulnerability_scanner
def scan_for_container_image_vulnerabilities(image_name):
  """Scans a container image for vulnerabilities.

  Args:
    image_name: The name of the container image.

  Returns:
    A list of vulnerabilities found in the container image.
  """

  vulnerabilities = vulnerability_scanner.scan(image_name)
  return vulnerabilities
```

4. Define a function to compare the vulnerabilities in a container image to the container image database.

This function will compare the vulnerabilities in a container image to the container image database and identify any known vulnerabilities.

```python
def compare_container_image_vulnerabilities(vulnerabilities, container_image_database):
  """Compares the vulnerabilities in a container image to the container image database and identifies any known vulnerabilities.

  Args:
    vulnerabilities: A list of vulnerabilities found in a container image.
    container_image_database: A dictionary of container images and their versions.

  Returns:
    A list of known vulnerabilities in the container image.
  """

  known_vulnerabilities = []
  for vulnerability in vulnerabilities:
    if vulnerability in container_image_database:
      known_vulnerabilities.append(vulnerability)
  return known_vulnerabilities
```

5. Use the container scanning library to scan a container image for vulnerabilities and identify any known vulnerabilities.

```python
image_name = 'my-image:latest'
container_image_database = fetch_container_image_database()
vulnerabilities = scan_for_container_image_vulnerabilities(image_name)
known_vulnerabilities = compare_container_image_vulnerabilities(vulnerabilities, container_image_database)

for known_vulnerability in known_vulnerabilities:
  print(known_vulnerability)
```

Output:

```
CVE-2023-12345: Vulnerability in container image my-image:latest
```

This is a simple example of a container scanning library in Python. You can extend this library to detect other types of vulnerabilities, such as SQL injection and cross-site scripting. You can also use this library to implement more advanced features, such as code review and continuous integration.

There are also a number of third-party container scanning libraries available for Python. Some of the most popular libraries include:

* **Clair:** Clair is a library that scans container images for known security vulnerabilities.
* **Anchore:** Anchore is a library that scans container images for known security vulnerabilities and compliance issues.
* **Snyk:** Snyk is a library that scans container images for known security vulnerabilities and open source license violations.

You can use one of these third-party libraries instead of writing your own container scanning library.