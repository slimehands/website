export async function load({ params }) { 
	const post = await import(`../source-files/${params.slug}.svx`);
	const Content =  post.default;
	const slug =  params.slug;
	return {
		Content,
		slug
	};
	
	
}
