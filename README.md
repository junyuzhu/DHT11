树莓派使用DHT11传感器实现自动保存温度功能，并且在数据获取错误时将重复测量直到正常后写入到本地的hud_data.txt与tmp_data.txt中

具体实现方式
0 线材连接
DHT传感器有VCC，DATA，GND三个引脚，
VCC——————> +5V
DATA———————> gpio 4口
GND——————> GND 

获取代码
在命令行中输入
git clone https://github.com/junyuzhu/DHT11.git
克隆完成后,会出现一个DHT11文件夹在你的命令行当前目录


 

2.修改定时任务
在命令行中输入crontab -e ,第一次使用时crontab会要你选择一个编辑器，输入1或者2 选择你喜欢的编辑器
在编辑器中的字符串末尾添加
*/1 * * * * python /home/pi/DHT11/Save_data.py        #实现每分钟执行一次获取温湿度
注意这里的 /home/pi/DHT11 是我存放目录，如果你存放的目录并不是这里的话，请修改该位置

输入命令后保存退出后，这时命令行会有提示信息
然后 执行命令
sudo /etc/init.d/cron restart      
令到刚才输入的定时任务命令生效
这样只树莓派就会每分钟记录一次温度了
