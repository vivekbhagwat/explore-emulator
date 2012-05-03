require 'rubygems'
require 'sinatra'
require 'haml'
require 'json'

get '/' do
	cookie = nil
	if cookie.nil?
		redirect to('/login')
	end
	'did not redirect'
end

get '/login' do
	access_url = 'https://foursquare.com/oauth2/authenticate?client_id=EA2IBQTZ44BZZOFZSH4NRIK5NWNL0EINW3KOTTPFCYD4J4L2&response_type=code&redirect_uri=http://explore-emulator.herokuapp.com'
	request_url = 'https://foursquare.com/oauth2/access_token?client_id=EA2IBQTZ44BZZOFZSH4NRIK5NWNL0EINW3KOTTPFCYD4J4L2&client_secret=EJWCXQUCU01ZDWNVX1TTC34PQRUV5QK1O2G5Y34QU0UHEHPQ&grant_type=authorization_code&redirect_uri=http://vivekbhagwat.com&code=BYLUI4XNAN0NYSG40HCS1QVPLA5KHE1JSXULMB34JJACAO35'

	haml :login, :locals => {:connect_url => url}
end