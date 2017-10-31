import React from 'react'
import ReactDOM from 'react-dom'
import ExampleWork from './example-work'

const myWork = [
  {
    'title': 'Javascript Test Code Example',
    'href': 'https://github.com/MTRConsulting/ServerlessPortfolioWithReact/blob/master/code/__tests__/test-example-work.js',
    'desc': 'Test code for this portfolio web site using React (Facebook) & Enzyme (Airbnb).',
    'image': {
      'desc': 'example screenshot of a project involving code',
      'src': 'images/example1.png',
      'comment': ''
    }
  },
  {
    'title': 'AWS Lambda function to build/deploy site to S3',
    'href': 'https://github.com/MTRConsulting/ServerlessPortfolioWithReact/blob/master/code/upload-portfolio-lambda.py',
    'desc': 'This example demonstrates the use of Serverless architecture to build and deploy a static web site to AWS S3.',
    'image': {
      'desc': 'A Serverless Portfolio',
      'src': 'images/serverless-portfolio-with-react.png',
      'comment': ''
    }
  },
  {
    'title': '.Net Parallel Example',
    'href': 'https://gitlab.com/MajesticOpen/ContractManager/blob/master/ContractManager/ContractManager/ContractService.cs',
    'desc': 'Sample of code using the Parallel .NET library. The context is processing scanned contracts with an execution condition based on processor count.',
    'image': {
      'desc': 'example screenshot of parallel For loop',
      'src': 'images/ParallelExample3.png',
      'comment': `Code from a client engagement`
    }
  }
]
const element = (<ExampleWork work={myWork} />)
ReactDOM.render(element, document.getElementById('example-work'))
