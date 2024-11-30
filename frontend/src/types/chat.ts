export interface Chat {
	id: number;
	title: string;
	description?: string;
	url?: string;
	avatarUrl?: string;
	botIsAdmin?: boolean
}