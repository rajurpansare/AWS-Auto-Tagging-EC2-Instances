# AWS-Auto-Tagging-EC2-Instances
Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3

## 📌 Objective

Automatically tag EC2 instances upon launch using AWS Lambda and Boto3.

---

## 🛠️ Services Used

* AWS EC2
* AWS Lambda
* AWS IAM
* Amazon EventBridge
* CloudWatch Logs
* Boto3

---

## ⚙️ Steps Performed

### 1. EC2 Setup

* Verified EC2 instance launch capability

---

### 2. IAM Role

* Role Name: LambdaEC2AutoTagRole
* Policy: AmazonEC2FullAccess

---

### 3. Lambda Function

* Runtime: Python 3.14
* Function Name: EC2AutoTagger

---

### 4. Boto3 Script Features

* Extracted instance ID from event
* Tagged instance with:

  * CreatedOn (current date)
  * Owner (custom tag)

---

### 5. EventBridge Rule

* Rule Name: EC2LaunchAutoTagRule
* Trigger:

  * EC2 Instance State = running
* Target:

  * Lambda function

---

### 6. Testing

* Launched new EC2 instance
* Verified automatic tagging

---

## 📊 Output

* EC2 instances automatically tagged on launch

---

## 📸 Screenshots

<img width="1493" height="212" alt="image" src="https://github.com/user-attachments/assets/ed60b2a6-d4c4-44ff-b417-b6eeb659923e" />


<img width="1471" height="662" alt="image" src="https://github.com/user-attachments/assets/70a53223-d987-409b-810b-f956bef736d8" />


* IAM role
* Lambda function
* EventBridge rule
* EC2 instance with tags

---

## ✅ Conclusion

Successfully automated EC2 instance tagging using Lambda and EventBridge.

---

