import { Search } from 'lucide-react';
import React from 'react';

type Props = {
  onSearch: (query: string) => void;
  searchTerm: string;
};

export const MembersSearch: React.FC<Props> = ({ onSearch, searchTerm }) => {
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    onSearch(e.target.value);
  };

  return (
    <div className="members__inputs">
      <Search />
      <input
        placeholder="Поиск..."
        type="text"
        maxLength={20}
        value={searchTerm}
        onChange={handleChange} 
      />
    </div>
  );
};
