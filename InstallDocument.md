# 安装 / 部署 QBEA

首先你需要准备：
- Python 环境
  - 项目编写时使用的是`Python 3.12`，不考虑库兼容性，最早可能可以支持到`Python 3.6`版本，但建议使用`Python 3.12`部署。
- 环境合适的服务器，本地设备也可以。

请在需要部署的设备上 Clone 整个仓库或直接使用 Release (更为稳定) 部署

## 本地部署

启动`launch.py --local`即可，随后按照 Console UI 配置，如果需要附着于本地 NT QQ，请启动`launch.py --local --attach-to-local-ntqq`

## 服务器部署

> 安全起见，建议预配 SSL 证书，不建议 HTTP 直连。

在服务器启动`launch.py --server --remote-port 16383`即可，`16383`可以替换成需要的端口。注意在云服务器安全组&服务器防火墙放行`16383`接口。

在本地启动`launch.py --remote-connect 127.0.0.1:16383`即可，`127.0.0.1:16383`替换成服务器 IP&端口，随后按照 Console UI 配置。