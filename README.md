# Toolbox 🧰

🧰 Tổng hợp các tools 🛠️ & scripts 📝 cho Cloud engineer ☁️

## Mục lục

- [Toolbox 🧰](#toolbox-)
  - [Mục lục](#mục-lục)
  - [Scripts phân loại theo vendors và services](#scripts-phân-loại-theo-vendors-và-services)
    - [AWS](#aws)
      - [EC2](#ec2)
      - [S3](#s3)
    - [Azure](#azure)
      - [DevOps](#devops)
      - [Service Bus](#service-bus)

## Scripts phân loại theo vendors và services

### AWS

#### EC2

- **[resize_volume.sh](aws/ec2/resize_volume.sh)** - Resize volume của disk cho EC2 instance

#### S3

- **[list_file_older_than_n_days.py](aws/s3/list_file_older_than_n_days.py)** - Liệt kê các files có thời gian upload trên N ngày của S3

### Azure

#### DevOps

- **[change_tags.py](azure/devops/change_tags.py)** - Thay đổi tag của machine trong deployment group của Azure DevOps

#### Service Bus

- **[purge_dlq.py](azure/service_bus/purge_dlq.py)** - Purge các messages của Death Letter Queue (DLQ) của Service Bus
