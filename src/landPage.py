def landPage():
    """
    Returns an HTML as FrontPage
    """

    return """<h1 style="color: #5e9ca0;">Welcome to chat emotion API!</h1>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<h2 style="color: #2e6c80;">Please go to the following endpoints:</h2>
<table style="height: 219px; border-color: #000000;" width="653">
<tbody>
<tr>
<td style="width: 318.5px; background-color: #ffa500;">ENDPOINT</td>
<td style="width: 318.5px; background-color: #ffa500;">ACTION</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;/user/create/&quot;"><a href="/user/create">"/user/create/"</a></h3>
</td>
<td style="width: 318.5px;">CREATE an USER</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;/chat/create/&quot;"><a href="/chat/create">"/chat/create/"</a></h3>
</td>
<td style="width: 318.5px;">CREATE a CHAT with the USERS you choose. They have to go in the User field separated by "," (commas)</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;/chat/&lt;'chat_id'&gt;/adduser&quot;" style="font-style: normal; font-variant-caps: normal; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; box-sizing: border-box; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; line-height: 1; color: #000000; margin: 0.777em 0px 0px; font-size: 18.00400161743164px; caret-color: #000000;">"/chat/&lt;'chat_id'&gt;/adduser"</h3>
</td>
<td style="width: 318.5px;">ADD an USER to the &lt;'chat_id'&gt; CHAT</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;/chat/&lt;'chat_id'&gt;/addmessage&quot;" style="font-style: normal; font-variant-caps: normal; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; box-sizing: border-box; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; line-height: 1; color: #000000; margin: 0.777em 0px 0px; font-size: 18.00400161743164px; caret-color: #000000;">"/chat/&lt;'chat_id'&gt;/addmessage"</h3>
</td>
<td style="width: 318.5px;">ADD a MESSAGE written by the USER you choose to the &lt;'chat_id'&gt; CHAT</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;/chat/&lt;'chat_id'&gt;/list&quot;" style="font-style: normal; font-variant-caps: normal; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; box-sizing: border-box; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; line-height: 1; color: #000000; margin: 0.777em 0px 0px; font-size: 18.00400161743164px; caret-color: #000000;">"/chat/&lt;'chat_id'&gt;/list"</h3>
</td>
<td style="width: 318.5px;">RETURNS ALL the messages from &lt;'chat_id'&gt; CHAT</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;/chat/&lt;'chat_id'&gt;/sentiment&quot;" style="font-style: normal; font-variant-caps: normal; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; box-sizing: border-box; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; line-height: 1; color: #000000; margin: 0.777em 0px 0px; font-size: 18.00400161743164px; caret-color: #000000;">"/chat/&lt;'chat_id'&gt;/sentiment"</h3>
</td>
<td style="width: 318.5px;">RETURNS the SENTIMENT of &lt;'chat_id'&gt; CHAT</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;/user/&lt;'user'&gt;/sentiment&quot;" style="font-style: normal; font-variant-caps: normal; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; box-sizing: border-box; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; line-height: 1; color: #000000; margin: 0.777em 0px 0px; font-size: 18.00400161743164px; caret-color: #000000;">"/user/&lt;'user'&gt;/sentiment"</h3>
</td>
<td style="width: 318.5px;">RETURNS the SENTIMENT of &lt;'user'&gt; USER in all CHATS</td>
</tr>
<tr>
<td style="width: 318.5px;">
<h3 id="&quot;user/&lt;'user'&gt;/recommend&quot;" style="font-style: normal; font-variant-caps: normal; letter-spacing: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: auto; word-spacing: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px; text-decoration: none; box-sizing: border-box; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-weight: bold; line-height: 1; color: #000000; margin: 0.777em 0px 0px; font-size: 18.00400161743164px; caret-color: #000000;">"user/&lt;'user'&gt;/recommend"</h3>
</td>
<td style="width: 318.5px;">RETURNS the USER that MATCHES the best with &lt;'user'&gt; USER.</td>
</tr>
<tr>
<td style="width: 318.5px;">&nbsp;</td>
<td style="width: 318.5px;">&nbsp;</td>
</tr>
</tbody>
</table>
    """