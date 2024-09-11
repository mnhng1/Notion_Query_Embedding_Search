from django.shortcuts import redirect
import asyncio

def notion_login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated via Notion
        if not request.session.get('is_authenticated'):
            # If not, redirect them to the Notion login page

        
        # If authenticated, proceed with the original view
        
            return  view_func(request, *args, **kwargs)
        
            
    
    return _wrapped_view
    
  