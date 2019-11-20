import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

@IonicPage()
@Component({
  selector: 'page-search',
  templateUrl: 'search.html'
})
export class SearchPage {

  slideOpts = {
    initialSlide: 1,
    speed: 400,
    pager: true
  };

  constructor() { }

}
