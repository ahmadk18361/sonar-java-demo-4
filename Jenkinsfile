pipeline {
    agent any

    tools {
        maven 'Maven'
        jdk 'jdk-17'
    }

    environment {
        SONARQUBE_SERVER = 'SonarCloud' // Must match Jenkins config name exactly
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ahmadk18361/sonar-java-demo-4.git'
            }
        }
        
        stage('Remediate Vulnerabilities') {
            steps {
                bat 'remediation_cve_2021_33813.py'
            }
        }
        
        stage('Build') {
            steps {
                bat 'mvn clean package'
                bat 'git config --global user.email "jenkins@example.com"'
                bat 'git config --global user.name "Jenkins"'
                bat 'git add .'
                bat 'git commit -m "Apply automatic fix to hardcoded credentials" || exit 0'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${Sonar-cve's}") {
                    withCredentials([string(credentialsId: '2ndsonar', variable: 'SONAR_TOKEN')]) {
                       bat """
                            mvn clean verify sonar:sonar \
                              -Dsonar.projectKey=Sonar-cve-s \
                              -Dsonar.projectName='Sonar-cve's' \
                              -Dsonar.host.url=http://localhost:9000 \
                              -Dsonar.token=sqa_f185c86f9cfcdf5600835234e95de3b879833346
                            """
                    }
                }
            }
        }
    }
}
