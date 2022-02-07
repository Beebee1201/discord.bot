const Discord = require("discord.js")
const bot = new Discord.Client()


bot.on('ready', () => {
    console.log(bot.user.tag)

})



bot.login('ODYwMDY0NDA0MTY3MTk2Njgz.YN1zZQ.MlyjSaaMUClHDb9V9s2FcApcoSI')

bot.on('message',msg =>{
    switch(msg.content ){
        case '嘿嘿':
            msg.channel.send("嘿你老母")
            break
        case '進來':
            voiceChannel.join()
            .then(connection => console.log('Connected!'))
            .catch(console.error);
    }
   

})