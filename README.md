# tybbs-checkin

这是一个用于自动签到 [V次元](https://bbs.66ccff.cc) 的 Python 脚本。通过 GitHub Actions 实现每天自动签到。

## 免责声明

- 本项目仅供学习和研究使用。请确保在遵守相关法律法规及目标网站的服务条款的前提下使用本项目。

- 开发者不对任何因使用本项目而产生的直接或间接后果负责，包括但不限于账户封禁、账户被盗、数据丢失或其他任何形式的损失。

## 功能

- 每天自动签到
- 使用 GitHub Actions 实现自动化

## 使用方法

### 1. Fork 该仓库

点击右上角的 `Fork` 按钮，将该仓库 Fork 到你的 GitHub 账户中。

![1](/.github/pics/1.png)

### 2. 配置 Cookie

#### 获取我的 Cookie

1. 打开 Chrome 浏览器并登录到 [bbs.66ccff.cc](https://bbs.66ccff.cc)。
2. 登录后，按下 `F12` 键或右键点击页面并选择 `检查`，打开开发者工具。
3. 在开发者工具窗口中，点击顶部的 `Application` (`应用程序`) 标签。
4. 在左侧的 `Storage` (`存储`) 下找到并点击 `Cookies`，然后选择 `https://bbs.66ccff.cc`。
5. 在右侧窗口中，你将看到所有与该网站相关的 Cookie。找到名为 `wordpress_sec_******` 的 Cookie 及其对应的值。
6. 复制 Cookie 的名称 (通常以 `wordpress_sec_` 开头)，与整个 Cookie 值，**并将其妥善保管（否则会有账号被盗的风险）**。
  ![2](/.github/pics/2.png)

#### 将 Cookie 配置为 GitHub Secrets

1. 导航到你的 GitHub 仓库
2. 点击 `Settings` (设置)。
3. 在左侧菜单中找到 `Secrets and variables`，然后点击 `Actions`。
4. 点击 `New repository secret` 按钮。
   ![3](/.github/pics/3.png)
5. 添加一个新的秘密，名称为 `BBS_COOKIE`，并将你的 Cookie 值粘贴到“值”字段中。
  注意格式：假设你的 Cookie 名为 `wordpress_sec_a12345` ，复制到的值为 `abcdef`，则需要粘贴的格式为 `wordpress_sec_a12345=abcdef`
  ![4](/.github/pics/4.png)

### 3. 配置 GitHub Actions

GitHub Actions 配置文件位于 `.github/workflows/run.yml`。默认情况下，该文件已经配置为每天 6:30 CST 自动运行。如果你需要修改运行时间，可以编辑该文件中的 `cron` 表达式。

### 4. 手动触发工作流

如果你想立即测试脚本，可以手动触发 GitHub Actions 工作流：

1. 进入你的 GitHub 仓库页面。
2. 点击 `Actions` 标签。
3. 如果显示 `Workflows aren't being run on this forked repository`，请点击 `I understand my workflows, go ahead and enable them` 以启用 Actions。
   ![5](/.github/pics/5.png)
4. 选择 `Checkin` 工作流。
5. 点击 `Run workflow` 按钮
6. 选择分支并点击 `Run workflow`。
   ![6](/.github/pics/6.png)

### 5. 查看签到结果

工作流运行结束后，你可以在 `Actions` 的 `Summary` 标签页中查看运行日志，确认签到是否成功。
  ![7](/.github/pics/7.png)

如果签到失败，将会提示 `签到失败！ 400 0`。请检查先前的步骤是否正确，如仍无法解决，请通过提交 Issue 寻求帮助。

## 贡献

欢迎任何形式的贡献！你可以通过提交 Issue 或 Pull Request 来帮助改进这个项目。<img width="25%" src="/.github/pics/8.png" alt="logo">

## 许可证

该项目使用 MIT 许可证。详见 [LICENSE](/LICENSE) 文件。
