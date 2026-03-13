from src.main import Main
from src.components.bot import Bot

if __name__=="__main__":
    print("started")
    ma=Main()
    bot=Bot()


    def ask(question):
        print("say your question")
        
        context=ma.data_loader(question=question)

        res=bot.initate_bot(question=question,context=context,session_id="1")
        return res

    question=input("enter the question :")
    res=ask(question=question)
    print(res)