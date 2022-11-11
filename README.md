# Toolbox 🧰

🧰 Tổng hợp các tools 🛠️ & scripts 📝 cho Cloud/DevOps engineer ☁️

---

<a href="https://webuild.community">
	<img src="https://raw.githubusercontent.com/webuild-community/badge/master/svg/made.svg" />
</a>

---

<p float="left">
	<a href="https://vntechies.dev">
		<img src="https://img.shields.io/badge/vntechies.dev-111827?style=for-the-badge&logo=About.me&logoColor=ea580c" />
	</a>
	<a href="https://discord.gg/YecagKUqpS">
		<img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" />
	</a>
	<a href="https://fb.me/vntechies">
		<img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" />
	</a>
	<a href="https://github.com/vntechies">
		<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" />
	</a>
	<a href="https://twitter.com/vn_techies">
		<img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" />
	</a>
	<a href="https://www.youtube.com/channel/UCl_qarJJ3dES5X_CRGQjNLw">
		<img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
	</a>
</p>

---

## Mục lục

- [Toolbox 🧰](#toolbox-)
	- [Mục lục](#mục-lục)
	- [Scripts phân loại theo vendors và services](#scripts-phân-loại-theo-vendors-và-services)
		- [AWS](#aws)
			- [EC2](#ec2)
			- [S3](#s3)
		- [Azure](#azure)
			- [DevOps](#devops)
			- [Search Service](#search-service)
			- [Service Bus](#service-bus)
	- [k8s](#k8s)
	- [Blogs](#blogs)
	- [Người đóng góp](#người-đóng-góp)
	- [Ủng hộ VNTechies ❤️‍🔥](#ủng-hộ-vntechies-️)

## Scripts phân loại theo vendors và services

### AWS

#### EC2

- **[resize_volume.sh](aws/ec2/resize_volume.sh)** - Resize volume của disk cho EC2 instance
- **[unassociated_eip.sh](aws/ec2/unassociated_eip.sh)** - Lấy danh sách các IP address chưa được gắn với tài nguyên

#### S3

- **[list_file_older_than_n_days.py](aws/s3/list_file_older_than_n_days.py)** - Liệt kê các files có thời gian upload trên N ngày của S3
- **[empty_delete_bucket.sh](aws/s3/empty_delete_bucket.sh)** - Làm trống (xoá tất cả files) và xoá bucket **mãi mãi**

### Azure

#### DevOps

- **[change_tags.py](azure/devops/change_tags.py)** - Thay đổi tag của machine trong deployment group của Azure DevOps

#### Search Service

- **[get_index.py](azure/search_service/get_index.py)** - Lấy thông tin của index của Azure Search service sử dụng Azure API
- **[delete_index.py](azure/search_service/delete_index.py)** - Xoá một index của Azure Search service sử dụng Azure API

#### Service Bus

- **[purge_dlq.py](azure/service_bus/purge_dlq.py)** - Purge các messages của Death Letter Queue (DLQ) của Service Bus

## k8s

- **[kubelet_check.sh](k8s/kubelet_check.sh)** - Lấy trạng thái của kubelet trên mỗi nodes của cluster

## Blogs

Các blog chứa các thủ thuật và thông tin hữu ích.

| RSS                                                                                                                       | Tên blog                                                                | Nội dung                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| <a href="http://blogs.aws.amazon.com/security/blog/feed/"> <img src="rss.png" width="22" height="22" > </a>               | **[AWS Security](https://aws.amazon.com/blogs/security)**               | Thông tin về các cập nhật , thông báo và bài đăng liên quan tới bảo mật, nhận dạng và compliance mới nhất của AWS. |
| <a href="http://blogs.aws.amazon.com/application-management/blog/feed/"> <img src="rss.png" width="22" height="22" > </a> | **[AWS DevOps](https://aws.amazon.com/blogs/devops)**                   | Các thông báo mới nhất của AWS DevOps và các bài viết hướng dẫn dạng how-to                                        |
| <a href="https://aws.amazon.com/blogs/architecture/feed/"> <img src="rss.png" width="22" height="22" > </a>               | **[AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/)** | Các bài viết về Architecture trên dựa trên những best practices                                                    |
| <a href="https://www.lastweekinaws.com/feed/"> <img src="rss.png" width="22" height="22" > </a>                           | **[Last week in AWS](https://www.lastweekinaws.com)**                   | Những cập nhật mới nhất trong tuần qua trên AWS                                                                    |
| <a href="https://www.hashicorp.com/blog/feed.xml"> <img src="rss.png" width="22" height="22" > </a>                       | **[HashiCorp Blog](https://www.hashicorp.com/blog)**                    | Tin tức mới nhất về các sản phẩm và hệ sinh thái của HashiCorp, các bài viết từ cộng đồng                          |
| <a href="https://kubernetes.io/feed.xml"> <img src="rss.png" width="22" height="22" > </a>                       | **[K8S Blog](https://kubernetes.io/blog/)**                    | Tin tức mới nhất liên quan tới K8S và hệ sinh thái xung quanh                   |


---

## Người đóng góp

Cảm ơn các đồng chí 🔥

[![Code Contributors](https://contrib.rocks/image?repo=vntechies/toolbox)](https://github.com/vntechies/toolbox/graphs/contributors)

Cách bạn có thể [đóng góp cho dự án này.](https://github.com/vntechies/toolbox/blob/main/.github/CONTRIBUTING.md)

---

## Ủng hộ VNTechies ❤️‍🔥

Nếu bạn thấy dự án này hữu ích, xin hãy ủng hộ VNTechies một ly cà phê. Các đóng góp sẽ được sử dụng để duy trì dự án mã nguồn mở này.

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/vntechies)
