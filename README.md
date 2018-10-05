# DHT11
树莓派使用DHT11传感器实现自动保存温度功能


d.py实现了获取温湿度与保存到tmp_data.txt与hud_data.txt
moving.py实现创建文件夹与移动温湿度文件到昨天时间文件夹的功能

其余两个.sh 文件是实现Linux规程任务所需要的执行文件


#####################
具体实现方式

在命令行中输入crontab -e

在末尾添加
*/1 * * * * (sh /home/pi/DHT11/run_tem.sh)      #实现每分钟执行一次获取温湿度

1 0 * * * (sh /home/pi/DHT11/moving.sh)         #实现每天的00：01创建文件夹，移动tmp_data.txt与hud_data.txt

保存退出后
执行

sudo /etc/init.d/cron restart  

否则你的定时命令不会执行
