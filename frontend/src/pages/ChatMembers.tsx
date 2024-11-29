import React from 'react';
import { ChatListMembers } from '../components/index';

const members = [
  {
    id: 1,
    name: 'Какой-то мужик с рандомюзерапи',
    avatarUrl: 'https://randomuser.me/api/portraits/men/75.jpg',
  },
  {
    id: 2,
    name: 'Какая-то баба с рандомюзерапи',
    avatarUrl: 'https://randomuser.me/api/portraits/women/45.jpg',
  },
];

export const ChatMembers: React.FC = () => {
  return (
    <div className="chat-list-members">
      <ChatListMembers
        chatImageUrl="https://randomuser.me/api/portraits/men/35.jpg"
        chatMembersCount={555}
        chatName="ИмяЧатаКрутого"
        members={members}
      />
    </div>
  );
};
