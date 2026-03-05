pipeline {
    agent any

    environment {
        RENDER_API_KEY = credentials('render-api-key')
        DOCKER_CREDS   = credentials('dockerhub-creds')
    }

    stages {

        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Detect Changed Models') {
            steps {
                script {
                    env.CHANGED_MODELS = sh(
                        script: "git diff --name-only HEAD~1 HEAD | grep '^models/' | cut -d/ -f2 | sort -u | tr '\\n' ' ' || true",
                        returnStdout: true
                    ).trim()
                    echo "Changed models: ${env.CHANGED_MODELS}"
                }
            }
        }

        stage('Test Changed Models') {
            when { expression { env.CHANGED_MODELS?.trim() } }
            steps {
                script {
                    env.CHANGED_MODELS.trim().split().each { model ->
                        echo "Skipping local test - will test inside Docker"
                    }
                }
            }
        }

        stage('Docker Login') {
            when { expression { env.CHANGED_MODELS?.trim() } }
            steps {
                sh 'echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin'
            }
        }

        stage('Build, Push and Deploy') {
            when { expression { env.CHANGED_MODELS?.trim() } }
            steps {
                sh 'chmod +x deploy.sh'
                sh './deploy.sh $RENDER_API_KEY $BUILD_NUMBER'
            }
        }
    }

    post {
        success { echo " Pipeline succeeded! Deployed: ${env.CHANGED_MODELS}" }
        failure { echo " Pipeline failed for: ${env.CHANGED_MODELS}" }
        always  { sh 'docker logout || true' }
    }
}