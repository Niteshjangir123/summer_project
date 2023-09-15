import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import boto3

# AWS Configuration
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
region_name = 'us-east-1'  # Set your AWS region

# Create an EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

def create_ec2_instance():
    try:
        # Launch a new EC2 instance
        response = ec2.run_instances(
            ImageId='ami-12345678',  # Replace with your desired AMI ID
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',  # Replace with your desired instance type
            KeyName='your-key-pair-name'  # Replace with your key pair name
        )
        instance_id = response['Instances'][0]['InstanceId']
        messagebox.showinfo("Success", f"EC2 Instance {instance_id} launched successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

def create_s3_bucket():
    bucket_name = s3_bucket_entry.get()
    try:
        # Create an S3 bucket
        s3.create_bucket(Bucket=bucket_name)
        messagebox.showinfo("Success", f"S3 Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {str(e)}")

# Create the main application window
root = tk.Tk()
root.title("AWS Operations")

# Create a notebook widget to organize sections
notebook = ttk.Notebook(root)

# EC2 Section
ec2_frame = ttk.Frame(notebook)
notebook.add(ec2_frame, text="EC2")

ec2_label = ttk.Label(ec2_frame, text="Launch EC2 Instance", font=("Helvetica", 14))
ec2_button = ttk.Button(ec2_frame, text="Launch EC2", command=create_ec2_instance)

ec2_label.pack(pady=10)
ec2_button.pack(pady=10)

# S3 Section
s3_frame = ttk.Frame(notebook)
notebook.add(s3_frame, text="S3")

s3_label = ttk.Label(s3_frame, text="Create S3 Bucket", font=("Helvetica", 14))
s3_bucket_label = ttk.Label(s3_frame, text="Bucket Name:")
s3_bucket_entry = ttk.Entry(s3_frame)
s3_button = ttk.Button(s3_frame, text="Create S3 Bucket", command=create_s3_bucket)

s3_label.pack(pady=10)
s3_bucket_label.pack()
s3_bucket_entry.pack()
s3_button.pack(pady=10)

# Pack the notebook and start the main event loop
notebook.pack(fill='both', expand=True)
root.geometry("400x300")
root.mainloop()
