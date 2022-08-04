# HR-manager-discord-bot
A simple updated HR and manger bot for discord
<h1>Documentation</h1>
<h2>For user</h2>
<br>
<p>
It is a simple bot for use.  This bot create a bot that accepts a new user and open a channel for talking with
administration. As a administrator, you can:

</p>

<code>/create a hr_channel "Name_channel=optional"</code>  

<code>/create a report_channel "Name_channel=optional"</code>  

<code>/create an archive_channel "Name_channel=optional"</code>  

<code>/making_greetings_button</code>  

<br>
<p>
When you create a new a channel from list by command. This bot save their names. So you can stop working and start it working without settuping again.
<br>
To use this bot you need to get a special token for bot. You can get it from https://discord.com/developers.
There is a documentation for getting token and making bot  

In russia https://programka.com.ua/rukovodstvo/zvuk/kak-vkljuchit-rezhim-razrabotchika-discord  

In English: https://discordnet.dev/faq/basics/getting-started.html?tabs=dev-mode  

When a candidate come to your guild. In channel, where you set a command /making_greetings_button.
There are two buttons for candidate. Candidate or Report (Optional. Administrator can's change a name of buttons in Functionality/settings_components.json. Change attributes in settings_buttons_greetings). If candidate push one of those buttons.
A special channel opens him for talking with administration. This channel is private
</p>
