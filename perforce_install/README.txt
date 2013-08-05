How to use ReviewBoard.

Check you current python version on Windows.
For example: python2.7

Get p4 client tool from here: \p4_client_tool\windows\post-review2.7.xml
Put it in c:\codereview

Download rbtools-master.tar.gz
Extract rbtools-master.tar.gz to c:\codereview\rbtools-master
Under command line use next commands:

easy_install P4PythonInstaller
cd c:\codereview\rbtools-master
python setup.py install

Check, does postreview tool work?
python C:\Python27\Lib\rbtools-master\rbtools\postreview.py -d
if yes go to p4 client gui.

Login
Go to Tools->Manage Custom Tools...
Choose Custom Tools and click Import Tools...
Find c:\codereview\post-review2.7.xml
Choose it
Ok

Create changelist.
Click right button mouse on it. Choose send to codereview.

Codereview Board Tool.
Go to your ReviewBoard site and login under your user. Before create this user using admin permissions.

Click on Outgoing review. Find your review in the list. Click on it.
Choose branch, Bugs(defect), Groups, People(people who will be reveid your code).
Feel testing done section(show that test was passed or smth else)
Go to View Diff.
Check all your code and diff between your code and previous version.

If all is ok, click on Publish.
Now people, which you was choosed in People and people in Groups may check your changes.

What reviews can do.

They can find ll changelist request assign to them in http://<<your reviewboard site IP>>/dashboard/ 'to me' button.
Choose what you what to review and review it.
If you have some comment, for example in 7 line, click on 7 line and comment it.
Check all your comment in 'Review' button.
Fill 'Ship It' box if review owner can submit code.
Review owner should know that he can submit code after then all people who were set in 'People' section take 'Ship it' for his code review.

Have fun:) 








