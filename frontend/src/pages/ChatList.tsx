import '../sass/chatList.scss';
import ChatCard from '../components/ChatCard.tsx';

export const ChatList = () => {
    return (
        <div className="chat-list-container">
            <div className="header">
                <h1>Чаты</h1>
            </div>
            <div className="chat-cards">
                <ChatCard
                    chatName="ИмяЧатаКрутого"
                    description="КрутоеОписаниеЧата"
                    imageUrl="https://randomuser.me/api/portraits/men/75.jpg"
                />
                <ChatCard
                    chatName="ЕщеБолееКрутоеИмяЧата"
                    description="ЕщеБолееКрутоеОписаниеЧата"
                    imageUrl="https://randomuser.me/api/portraits/women/45.jpg"
                />
            </div>
        </div>
    )
};

export default ChatList;