pipeline {
    agent any

    environment {
        IMAGE_NAME = 'shabdoc/streamlit1-app:latest'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shabuddin-git/project-ci-practice.git'
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                    docker build -t "$IMAGE_NAME" .
                '''
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker-hub-cred',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login \
                            -u "$DOCKER_USERNAME" --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    docker push "$IMAGE_NAME"
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(credentials: ['streamlit-deploy-ssh-v2']) {
                    sh '''
                        ssh -o BatchMode=yes ubuntu@172.31.27.188 \
                        'docker pull shabdoc/streamlit1-app:latest &&
                         docker rm -f streamlit-app &&
                         docker run -d --name streamlit-app --restart unless-stopped -p 8501:8501 shabdoc/streamlit1-app:latest'
                    '''
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}