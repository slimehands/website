export const load = async ({ fetch }) => {
	const response = await fetch(`/search.json`);
	const posts = await response.json();

	return {
		posts
	};
};