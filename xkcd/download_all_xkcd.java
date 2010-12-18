import java.net.*;
import java.io.*;
import java.util.regex.*;

class download_all_xkcd {
	public static void main(String args[]) throws Exception{
		int i=0;int link=0;
		boolean val = true;
		String temp;
		String fin= null;
		String ext = null;
		String filename = null;
		while(link!=10){
			i++;
			try{
				System.out.println("Trying to process links..");
				URI uri = new URI("http://xkcd.com/"+i+"/");
				URL url = uri.toURL();
				BufferedReader br = new BufferedReader(new InputStreamReader(url.openStream()));
				Pattern pattern = Pattern.compile("http://imgs.xkcd.com/comics/(.)*[.](.)(.)(.)(\")");
				Matcher matcher;
				while(val){
					String b1 = br.readLine();
					matcher = pattern.matcher(b1);
					while(matcher.find()){
						temp = matcher.group();
						fin = fin.copyValueOf(temp.toCharArray(),0,temp.length()-1);
						val=false;
						ext = fin.substring(fin.length()-3);
						filename = i + "." +ext;
						new download(fin,filename);
					}
				}
			val = true;
			link=0;
			}catch(FileNotFoundException e){
			System.out.println("Checking more links...."+i);
			link++;
			if(link==10)
			{
				System.out.println("No more tries!!");
				break;
			}
		}
	}
}
}

class download{
	download(String link,String file) throws IOException,MalformedURLException{
		try{
			BufferedInputStream in = new java.io.BufferedInputStream(new URL(link).openStream());
			FileOutputStream fos = new java.io.FileOutputStream(file);
			BufferedOutputStream bout = new BufferedOutputStream(fos,1024);
			System.out.println("Downloading : "+ link + " to " + file );
			byte[] data = new byte[1024];
			int x=0;
			while((x=in.read(data,0,1024))>=0)
			{
				bout.write(data,0,x);
			}
			System.out.println("Downloaded as " + file);
			bout.close();
			in.close();
		}catch(IOException e){
			System.out.println("Link parsed Incorrectly");
		}
	}
}