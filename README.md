# Python Jenkins Pipeline Calculator

## Repository Structure
* Dockerfile: Builds a Jenkins environment with Docker CLI and required plugins.
* docker-compose.yml: Used to orchestrate Jenkins and other services.
* pipeline/: Contains the calculator source code, unit tests, and Jenkins pipeline configuration.
* pipeline/Jenkinsfile: Defines the Jenkins pipeline stages (clone, build, test, push).
* src/: Python source code and tests.
    * calc.py: Calculator logic (add, subtract, multiply, divide).
    * prog.py: Entry point for running the calculator.
    * test_calc.py: Unit tests for the calculator.
    * Dockerfile: Dockerization for the Python app.

## Getting Started

### Prerequisites

* Docker
* Docker Compose

### Setup

1. Setup Jenkins with Docker
```bash
docker build -t custom-jenkins .
```
2. Run Jenkins:
```bash
docker run -p 8080:8080 -p 50000:50000 --name jenkins -v /var/run/docker.sock:/var/run/docker.sock custom-jenkins
```
3. Access Jenkins:
Open your browser and navigate to `http://localhost:8080`.
4. Set up Jenkins Pipeline:
* Use the provided pipeline/Jenkinsfile to create a new pipeline job.
* Configure credentials as needed for DockerHub.

### Jenkins Pipeline Stages
* Clone: Pulls the latest code from the repository.
* Build: Compiles the Python source files.
* Test: Runs unit tests using pytest and archives results.
* Push Docker Image: Builds and pushes the calculator Docker image to DockerHub (requires credentials).

### Calculator Usage
You can run the calculator locally:
```bash
python3 pipeline/src/prog.py
```
Or run the tests:
```bash
pytest pipeline/src/test_calc.py
```
## References
* Original tutorial and code: [pipeline-calc](https://github.com/DataScientest/pipeline-calculatrice-Jenkins.git)
## License
MIT License