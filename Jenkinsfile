pipeline {
   agent any

   stages {
      stage('Build') {
        steps {
          echo 'Building...'
          build 'pipeline1'
        }
   }
   stage('Test') {
     steps {
        echo 'Testing...'
     }
   }
   stage('Deploy') {
     steps {
       echo 'Deploying...'
     }
   }
  }
}

